import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent  {
  details1:JSON;
  details2:JSON;
  details3:JSON;
  details4:JSON;
  details5:JSON;
  Type=['Casual Dining','Cafe','Quick Bites','Delivery', 'Mess', 'Dessert Parlor','Bakery','Pub','Takeaway','Fine Dining','Beverage Shop','Sweet Shop',
  'Bar','Confectionery','Kiosk','Food Truck','Microbrewery','Lounge','Food Court','UnknownRestType'];
  Cuisine=['North Indian','Mughlai','Chinese','Thai', 'Mexican', 'Italian', 'South Indian', 'Rajasthani', 'Andhra', 'Pizza', 'Continental',
 'Momos', 'Beverages', 'Fast Food', 'American', 'French', 'European', 'Burger', 'Desserts', 'Biryani', 'Street Food', 'Rolls',
 'Ice Cream', 'Healthy Food', 'Salad', 'Asian', 'Korean', 'Indonesian', 'Japanese', 'Goan', 'Seafood', 'Kebab', 'Steak', 'Mithai', 'Iranian',
 'Sandwich', 'Juices', 'Mangalorean', 'Vietnamese', 'Hyderabadi', 'Bengali', 'Arabian', 'BBQ', 'Tea', 'Afghani', 'Lebanese', 'Finger Food',
 'Tibetan', 'UnknownCuisine', 'Charcoal Chicken', 'Middle Eastern', 'Mediterranean', 'Wraps', 'Kerala', 'Oriya', 'Bihari', 'Roast Chicken',
 'Maharashtrian', 'Bohri'];
 Location=['Banashankari', 'Basavanagudi', 'Mysore Road', 'Jayanagar',
 'Kumaraswamy Layout', 'Rajarajeshwari Nagar', 'Vijay Nagar',
 'Uttarahalli', 'JP Nagar', 'South Bangalore', 'City Market',
 'Nagarbhavi', 'Bannerghatta Road', 'BTM', 'Kanakapura Road'];
 Rating=[1,2,3,4,5];
 Voting=[100,200,300,400,500,600,700,800,900,1000];
  online:number;
  book:Number;
  valueRating:Number;
  valueVote:Number;
  cost:Number;
  nameType:string;
  nameCuisine:string;
  nameLocation:string;
  arrType = Array<number>(20).fill(0);
  arrCuisine = Array<number>(59).fill(0);
  arrLocation = Array<number>(15).fill(0);
  list=[];
  data=['Name','Rate','Votes','Online','Location','Cuisines','RestType']
  constructor(private httpClient:HttpClient){ }
  sendPost()
    {
     
      let indexType =this.Type.indexOf(this.nameType);
      this.arrType[indexType]=1;
      let indexCuisine =this.Cuisine.indexOf(this.nameCuisine);
      this.arrCuisine[indexCuisine]=1;
      let indexLoc =this.Location.indexOf(this.nameLocation);
      this.arrLocation[indexLoc]=1;
      this.httpClient.post('http://127.0.0.1:12345/predict',
      {
        online:this.online,
        book:this.book,
        valueRating:this.valueRating,
        valueVote:this.valueVote,
        cost:this.cost,
        arrType :this.arrType,
        arrCuisine: this.arrCuisine,
        arrLocation: this.arrLocation
      })
      .subscribe
      (
        (data:any[])=>{
          this.details1=JSON.parse(data[0]);
          this.details2=JSON.parse(data[1]);
          this.details3=JSON.parse(data[2]);
          this.details4=JSON.parse(data[3]);
          this.details5=JSON.parse(data[4]);
          this.list=[this.details1,this.details2,this.details3,this.details4,this.details5]
          
        }
      )
      }
 
    }
