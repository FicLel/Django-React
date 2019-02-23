import React, { Component } from 'react';

export default class Articles extends Component{
  constructor(props){
    super(props);
    this.state = {articles: [],};
  }

 componentDidMount(){
   fetch('http://127.0.0.1:8000/api/?format=json').then(results => {
     return results.json();
   }).then(articles => {
     this.setState({articles});

   });
 }

render(){
  const { articles} = this.state;
  let results = articles.map( value => <div>{value.title}</div>);
  return (
    <div>
    {results}
    </div>
  );
}

}
