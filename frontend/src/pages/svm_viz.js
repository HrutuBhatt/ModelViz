import React, {useState} from "react"
import Stemming from "../components/stemming"
import Vectorize from "../components/vectorize"
import './svm_viz.css';
const SVM = ()=>{
    const [message, setMessage] = useState('"Running, runner, and ran are different forms of the word run."');
    const [stemmedText, setStemmedText] = useState("")
    return(
        <div className="container2">
            <h2>Preprocessing: </h2>
            <Stemming message={message} setMessage={setMessage} stemmedText={stemmedText} setStemmedText={setStemmedText} />
            <h5>Here TfidfVectorizer is used for Spam Text Detection</h5>
            {/* <Vectorize stemmedText={stemmedText}/> */}
            
        </div>
    )
}

export default SVM;