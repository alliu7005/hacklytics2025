const path = require('path');

module.exports = {
  entry: path.resolve(__dirname, './static/src/firebase-config.js'),
  // The location of the build folder described above
  output: {
    path: path.resolve(__dirname, './static/dist'),
    filename: 'bundle.js'
  },
  devtool: "inline-source-map",
};