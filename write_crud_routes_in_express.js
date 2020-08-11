// Provides basic CRUD routes for deleteing

const express = require('express');
const app = express();

// Serves Express Yourself website
app.use(express.static('public'));


// Assumes the below exist somewhere else - not in the scope of this example
const { getElementById, getIndexById, updateElement, createElement } = require('./utils');

const organizations = []; // Fill this with data however you want, or use an ORM like mongoose
const PORT = process.env.PORT || 4001;
app.use(express.static('public')); // Allow Express to serve the static site elements


// ==== Organizations CRUD

// Read/GET
app.get('/organizations', (req, res, next) => {
  res.send(organizations);
});

app.get('/organizations/:id', (req, res, next) => {
  const thisorganization = getElementById(req.params.id, organizations);
  if (thisorganization) {
    res.send(thisorganization);
  } else {
    res.status(404).send("Not found");
  }
});


// Update/PUT
app.put('/organizations/:id', (req, res, next) => {
  const updatesToApply = req.query;
  if (organizations[req.params.id]) {
    const thisorganization = updateElement(req.params.id, updatesToApply, organizations);
    res.send(thisorganization);
  } else {
    res.status(404).send("Not found");     
  }
});

// Create/POST
app.post('/organizations', (req, res, next) => {
  const neworganization = createElement('organizations', req.query);
  if (neworganization) {
    organizations.push(neworganization);
    res.status(201).send(neworganization);
  } else {
    res.status(400).send("Couldn't create the object with the parameters provided");
  }
});


// Delete/DELETE
app.delete('/organizations/:id', (req, res, next) => {
  const organizationIndex = getIndexById(req.params.id, organizations);
  if (organizationIndex != -1) {
    organizations.splice(organizationIndex, 1);
    res.status(204).send();
  } else {
    res.status(404).send();
  }
});


// ===== Port assignment for listener
app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`); 
});