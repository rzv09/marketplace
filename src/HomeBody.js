import React from 'react';
import Item from './Item.js';
import Container  from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Stack from 'react-bootstrap/Stack';
import data from './data.js';
import './HomeBody.css';

function HomeBody() {
      return (
    //   <Container>
    <div className="homeBody">
      <Row xs={1} md={4} className="g-4" >
      {data.map((item, index) => (
        <Col>
                <Item
                key={index}
                id={index}
                title={item.product.object_name}
                description={item.product.description}
                date={item.time_added}
                />  
        </Col>
        ))}
      </Row>   
    </div>
     )
       
}

export default HomeBody;