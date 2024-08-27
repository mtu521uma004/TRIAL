import React from 'react'

function Form() {
  return (
    <div>
        <form>
            <label>Username:</label>
            <input type="text" id="username" name="username"/><br></br>
            <label>Password:</label>
            <input type="password" id="password" name="password"/><br></br>
        </form>
    </div>
  );
}

export default Form;

