import React from 'react';
import {Navbar} from 'react-bootstrap';
import HomeBody from './HomeBody.js';

const Home = () => {
  return (
    <div>
    <Navbar bg="primary" variant="dark" className="justify-content-center">
        <Navbar.Brand>Student Marketplace</Navbar.Brand>
    </Navbar>
    <div class="grid text-center">
        <HomeBody/>
    </div>
    </div>
  )
}

export default Home