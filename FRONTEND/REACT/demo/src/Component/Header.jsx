// import React from 'react'

// function Header() {
//   return (
//     <div>
//         <h1>hii user!!</h1>
//         <h2>Enter your username and password</h2>
//     </div>
//   );
// }

// export default Header;

import React from "react";

const Header = () => {
  return (
    <div>
      <h1>hii user!!</h1>
      <h2>Enter your username and password</h2>
      <Footer name="mahima" />
    </div>
  );
};
const Footer = (e) => {
  return (
    <div>
      <h1>hii {e.name}!!</h1>
      <h2>Enter your username and password</h2>
    </div>
  );
};

export default Header;

// import React from 'react'

// function Header() {
//   return (
//     <div>
//       <h1>hii user!!!</h1>
//     </div>
//   )
// }

// export default Header
