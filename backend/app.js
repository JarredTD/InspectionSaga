// const http = require("http")
// const url = require("url")

const express = require("express");
const app = express();

app.get("/inspection_data", function(req, res) {
    res.send(true)
});

app.use(express.static('frontend/public/'));

app.listen(3000, () => {
    console.log("Server started on port 3000");
});
