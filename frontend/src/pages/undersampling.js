import React from "react"
import imbalance from '../static/imbalance_spam_ham.png';
import bargraph from '../static/imbalance_bar_graph.png';
import text_len from '../static/text_len.png';
const Undersampling = ()=>{
    return (
        <div className="container2">
            <h4>Original Dataset</h4>
            <p>Imbalanced Ham v/s Spam Messages</p><br/>
            <img src={imbalance} alt="Imbalanced Dataset"/>
            <br/><br/>
            <h4>Ham and Spam message length comparision</h4><br/>
            <img src={bargraph} alt="Imbalanced Dataset"/>
            <br/><br/>
            <h4>After Undersampling the data: </h4><br/>
                    <b>Count</b><br/>
                    Category	<br/>
                    spam:	 924 <nr/>
                    ham:     924 <br/>
                    <br/>
            <h4>Text length of spam and ham message: </h4>
            <img src={text_len} alt="Text Length"/><br/>
            <p>Spam messages are lengthier than ham (on an average : from 0 to 200)</p>
        </div>
    )
}
export default Undersampling