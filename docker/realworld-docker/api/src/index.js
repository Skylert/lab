const express = require("express");

const port = process.env.PORT;
const host = process.env.HOST;
console.log("PORT", port);
const app = express();

app.get("/test", (req, res) => {
  res.send("Our API server is working correctly");
});

app.listen(port, () => {
  console.log(`Started API service on port ${port}`);
  console.log(`Our host is ${host}`);
});
