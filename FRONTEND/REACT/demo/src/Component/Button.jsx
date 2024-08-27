import React from 'react'

const Button = (a) => {
  return (
    <div>
        {/* <button> Sign in </button>bb   */}
      <h4>{a.name}</h4>
      <h1>{a.age}</h1>
      <td>{a.text}</td>
    </div>
  );
}

export default Button;
