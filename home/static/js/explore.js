var subdomains = [

  {selection:"no", name:"AI", link:""},
  {selection:"no", name:"CyberSecurity",link:""},
  {selection:"no", name:"Big-Data Analytics", link:""},
  {selection:"no", name:"BioInformatics", link:""},
  {selection:"no", name:"Machine Learning", points:"20", link:""},
  {selection:"no", name:"Cryptography", points:"1", link:""}

];

var app = angular.module("myApp",[]);
   app.controller("myCtrl", function($scope){

      $scope.myObj = subdomains;

      $scope.myObj2 = [
        {usually:"10 min", question:"How To Develop a Chatbot From Scratch", link:"../dynamic_programming/questions/Sherlock and Coprime Subset.html", duration:"15 Min Read", background:"https://cdn-images-1.medium.com/max/1200/0*oz2e-hQtsHOWzoB4."},
        {usually:"20 min", question:" 5 Ways to Make AI Work for Your Organization",link:"../dynamic_programming/questions/Sherlock and Coprime Subset.html", duration:"5 Min Read",background:"https://images.idgesg.net/images/article/2018/10/ai_artificial-intelligence_circuit-board_circuitry_mother-board_nodes_computer-chips-100777423-large.jpg"},
        {usually:"30 min", question:"Manna's First Name", link:"../dynamic_programming/questions/Sherlock and Coprime Subset.html", duration:"15 Min Read", background: "../assets/images/image-1-1200x667.jpg"},
        {usually:"35 min", question:"Simple Search", link:"../dynamic_programming/questions/Sherlock and Coprime Subset.html", duration:"15 Min Read", background:"../assets/images/image-1-1200x667.jpg"},
        {usually:"15 min", question:"BooBoo and Upsolving", points:"20", link:"../dynamic_programming/questions/Sherlock and Coprime Subset.html", duration:"15 Min Read", background:"../assets/images/image-1-1200x667.jpg"},
        {usually:"20 min", question:"Gaurav And Sub-array", points:"1", link:"../dynamic_programming/questions/Sherlock and Coprime Subset.html", duration:"15 Min Read", background:"../assets/images/image-1-1200x667.jpg"},
        {usually:"10 min", question:"Round Table Meeting", points:"0", link:"../dynamic_programming/questions/Sherlock and Coprime Subset.html", duration:"15 Min Read", background:"../assets/images/image-1-1200x667.jpg"},
        {usually:"25 min", question:"Sumit and Chocolates", link:"../dynamic_programming/questions/Sherlock and Coprime Subset.html", duration:"15 Min Read", background:"{% static '/assets/images/image-1-1200x667.jpg' %}"},
        {usually:"20 min", question:"Puzzled Grid", link:"../dynamic_programming/questions/Sherlock and Coprime Subset.html", duration:"15 Min Read", background:"../assets/images/image-1-1200x667.jpg"}
     ]
});