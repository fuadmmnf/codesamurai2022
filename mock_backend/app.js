const jsonServer = require('json-server');
const app = jsonServer.create();
const router = jsonServer.router('db.json'); // <== Will be created later
const middlewares = jsonServer.defaults();
const port = process.env.PORT || 3200; // <== You can change the port

app.use(middlewares);
app.use(router);

app.listen(port);