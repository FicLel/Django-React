import React, { Component } from 'react';
import axios from 'axios';
export default class Articles extends Component{
  constructor(props){
    super(props);
    this.state = {articles: []};
  }

 componentDidMount(){
   this.addData();
 }
 addData(){
  fetch('http://127.0.0.1:8000/api/?format=json').then(results => {
     return results.json();
   }).then(articles => {
     this.setState({articles});

   });
 }
 deleteData(id){
    axios.delete('http://127.0.0.1:8000/api/'+id+'/')
      .then(respuesta =>{
        this.addData();
      })
    
 }

render(){
  const { articles} = this.state;
  let results = articles.map( value => 
        <div class="cards__item">
          <div class="card">
            <div class="card__image card__image--fence"></div>
            <div class="card__content">
              <div class="card__title">{value.title}</div>
              <p class="card__text">{value.content}</p>
              <button class="btn red card__btn" id={value.id} onClick={() => this.deleteData(value.id) }>Eliminar</button>
            </div>
          </div>
        </div>
    );
  return (
    
    <div class="cards">
    {results}
    </div>
  );
}

}
