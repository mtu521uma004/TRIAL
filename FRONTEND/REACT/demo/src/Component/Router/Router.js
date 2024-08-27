import React from 'react'
import { BrowserRouter, Route, Routes } from "react-router-dom";   
import Homepage from '../Page/Homepage';
import Aboutpage from '../Page/Aboutpage';

const Router = () => {
  return (
    <div>
      {" "}
      <BrowserRouter>
        <Routes>
          <Route path="/Home" element={<Homepage />} />
          <Route path="/About" element={<Aboutpage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default Router