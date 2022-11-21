import React from 'react';

import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import car from './assets/2022_Honda_Civic.jpg';


function Item(props) {
  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src={props.image} />
      <Card.Body>
        <Card.Title>{props.title}</Card.Title>
        <Card.Text>{props.description}</Card.Text>
        <Button variant="outline-primary">BUY</Button>
      </Card.Body>
      <Card.Footer className="text-muted">Posted on {props.date}</Card.Footer>
    </Card>
  );
}

export default Item;