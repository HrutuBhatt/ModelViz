import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import './navbar.css'; 

const Navbar = () => {
  const [dropdownOpen, setDropdownOpen] = useState(false);

  const toggleDropdown = () =>{
    setDropdownOpen(!dropdownOpen)
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          ModelViz
        </Link>
        <ul className="navbar-links">
          <li>
            <Link to="/" className="navbar-link">Home</Link>
          </li>
          <li>
            <Link to="/detectspam" className="navbar-link">Detect Spam</Link>
          </li>
          <li>
            <Link to="/analytics" className="navbar-link">Analytics</Link>
          </li>
          {/* <li>
            <Link to="/whatsapp" className="navbar-link">WhatsApp</Link>
          </li> */}
          <li className='dropdown'>
            <span className='navbar-link dropdown-toggle' onClick={toggleDropdown}>
              Visualize
            </span>
            {dropdownOpen && (
              <ul className='dropdown-menu'>
                <li>
                  <Link to="/undersample" className='dropdown-link'>Undersampling</Link>
                </li>
                <li>
                  <Link to="/svm" className='dropdown-link'>SVM</Link>
                </li>
                <li>
                  <Link to="/nn" className='dropdown-link'>Neural Network</Link>
                </li>
                <li>
                  <Link to="/lstm" className='dropdown-link'>LSTM</Link>
                </li>
              </ul>
            )}
          </li>
          <li>
            <Link to="/about" className="navbar-link">About</Link>
          </li>
          
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
