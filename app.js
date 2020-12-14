var createError = require("http-errors");
var express = require("express");
var path = require("path");
var cookieParser = require("cookie-parser");
var logger = require("morgan");
var swig = require("swig");
var fs = require("file-system");
const { spawn } = require("child_process");

var indexRouter = require("./routes/index");
var usersRouter = require("./routes/users");
//var output;

var app = express();

// view engine setup
app.engine("html", swig.renderFile);
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "html");

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));

app.use("/", indexRouter);
app.use("/users", usersRouter);

app.post("/userinput", function(req, res) {
  console.log("hey");
  console.log(req.body);
  fs.writeFile(
    "userinput.txt",
    req.body.aptitude +
      "\n" +
      req.body.softskills +
      "\n" +
      req.body.ur +
      "\n" +
      req.body.cgpa +
      "\n" +
      req.body.domainknowledge +
      "\n",
    function(err) {
      if (err) {
        console.log(err);
      }
      console.log("file created");
    }
  );
  const child = spawn("python", ["prediction.py"]);
  file = fs.createReadStream("userinput.txt");
  file.pipe(child.stdin);
  child.stdout.on("data", data => {
    console.log(data.toString("utf8"));
    let output_array = data.toString("utf8").split("\n");

    res.json({ success: true, answer: output_array });
  });

  // res.redirect("/");
});

app.get("/dashboarddata", function(req, res) {
  console.log("hry");
  const child = spawn("python", ["dashboarddata.py"]);
  child.stdout.on("data", data => {
    //console.log(data.toString("utf8"));
    let output_array = data.toString("utf8").split("\n");
    //console.log(output_array);
    let Yaxes = output_array[0].split(",");
    let Xaxes1 = output_array[3].split(",");
    let Xaxes2 = output_array[6].split(",");
    res.json({
      success: true,

      Xaxes1: Xaxes1,
      Xaxes2: Xaxes2,
      Yaxes: Yaxes
    });
  });
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get("env") === "development" ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render("error");
});

module.exports = app;
