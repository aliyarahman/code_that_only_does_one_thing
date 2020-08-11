const express = require('express');
const { seedElements, getElementById, createElement, updateElement, getIndexById } = require('./utils');

let expressions = [];
seedElements(expressions, 'expressions');

const expressionsRouter = express.Router();

// Get all expressions
expressionsRouter.get('/', (req, res, next) => {
  res.send(expressions);
});

expressionsRouter.get('/:id', (req, res, next) => {
    const expression = expressions[req.params.id];
    if (expression) {
      res.status(200).send(expression);
    } else {
      res.status(404).send();
    }
});

expressionsRouter.get('/:id', (req, res, next) => {
    const thisexpression = getElementById(req.params.id, expressions);
    if (thisexpression) {
      res.send(thisexpression);
    } else {
      res.status(404).send("Not found");
    }
});
  
  
  // Update/PUT
  expressionsRouter.put('/:id', (req, res, next) => {
    const updatesToApply = req.query;
    if (expressions[req.params.id]) {
      const thisexpression = updateElement(req.params.id, updatesToApply, expressions);
      res.send(thisexpression);
    } else {
      res.status(404).send("Not found");     
    }
  });
  
  // Create/POST
  expressionsRouter.post('/', (req, res, next) => {
    const newexpression = createElement('expressions', req.query);
    if (newexpression) {
      expressions.push(newexpression);
      res.status(201).send(newexpression);
    } else {
      res.status(400).send("Couldn't create the object with the parameters provided");
    }
  });
  

// Delete/DELETE
expressionsRouter.delete('/:id', (req, res, next) => {
    const expressionIndex = getIndexById(req.params.id, expressions);
    if (expressionIndex != -1) {
      expressions.splice(expressionIndex, 1);
      res.status(204).send(expressions[expressionIndex]);
    } else {
      res.status(404).send();
    }
});

module.exports = expressionsRouter;
