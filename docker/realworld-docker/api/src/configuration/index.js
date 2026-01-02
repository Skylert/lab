console.log("Environment variables:", {
  PORT: process.env.PORT,
  HOST: process.env.HOST,
  MONGO_URL: process.env.MONGO_URL,
});

module.exports.port = process.env.PORT;
module.exports.host = process.env.HOST;
module.exports.db = process.env.MONGO_URL;
