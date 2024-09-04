const express = require("express")
const sqlite3 = require("sqlite3").verbose()
const fs = require("fs")
const { parse } = require("csv-parse")

const app = express()
const db = new sqlite3.Database(":memory:")

db.serialize(() => {
  db.run(
    `CREATE TABLE datasets (
        id TEXT PRIMARY KEY, 
        doi TEXT,
        accession_number TEXT,
        repository TEXT, 
        keywords TEXT,
        citations INTEGER,
        title TEXT,
        abstract TEXT)`
  )

  db.run(`CREATE TABLE related_datasets (
        id TEXT PRIMARY KEY, 
        related_id TEXT)`)

  const query = `INSERT INTO datasets (
    id,
    doi,
    accession_number,
    repository,
    keywords,
    citations,
    title,
    abstract)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)`
  fs.createReadStream("metadata.csv")
    .pipe(parse({ delimiter: ",", from_line: 2 }))
    .on("data", (row) => {
      db.run(query, ...row)
    })

  console.log("done processing data...")
})

const getKeywords = (rows) => {
  if (!rows) return []

  const keywords = rows.map((x) => x.keywords)
  console.log(keywords)

  const groups = rows
    .map((x) => x.keywords?.split(","))
    .flat()
    .reduce((prev, curr) => {
      if (prev[curr]) prev[curr] += 1
      else prev[curr] = 1
      return prev
    }, {})

  console.log(groups)

  const entries = Object.entries(groups)
  entries.sort((x, y) => y[1] - x[1])

  const topEntries = entries.slice(0, 10)

  return Object.fromEntries(topEntries)
}

app.get("/datasets", (req, res) => {
  const keywords = req.query.keywords

  const query = `SELECT 
                    id,
                    title,
                    repository,
                    citations,
                    keywords
                FROM
                    datasets
                WHERE
                    keywords LIKE '%${keywords}%'`

  db.all(query, [], (err, rows) => {
    res.json({
      datasets: rows,
      keywords: getKeywords(rows),
    })
  })
})

app.get("/")

app.listen(3000, () => {
  console.log("API is running on PORT 3000")
})
