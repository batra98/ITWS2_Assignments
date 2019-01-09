function myArrayFilter(arr, callback) {

	var a = [];
	var c=0;
	for(let i=0;i<arr.length;i++)
	{
		
		let func=callback(arr[i],i,arr);
		if(func===true)
		{
			a[c]=arr[i];
			c++;
		}
	}
	return a;

}

function myArrayReduce(arr, callback, acc) {
	var accumulator
	if(acc==undefined)
	{
		accumulator=arr[0];
		for(let i=1;i<arr.length;i++)
		{
			accumulator=callback(accumulator,arr[i],i,arr);
		}

	}
	else
	{
		accumulator=acc;
		for(let i=0;i<arr.length;i++)
		{
			accumulator=callback(accumulator,arr[i],i,arr);
		}
	}
	

	return accumulator;
}

function myTreeReduce(inFunc, endFunc) {
		g=function(){
		let temp=arguments[0];
		if(temp.type==='end')
		{
			return endFunc(temp.value);
		}
		if(temp.type==='in')
		{
			//inFunc(g.arguments);
			//g(g.arguments['left']);
			//g(g.arguments['right']);
			return inFunc(temp.value,g(temp.left),g(temp.right));
		}
	}
	return g;

}

function myTreeSize(tree) {
	//var count=1;
	return myTreeReduce((a,b,c)=>1+b+c,()=>1)(tree);


}

function myTreeTraversal(type) {
	var a = [];
	if(type==='pre')
	{
		console.log(type);
		return g = function(){

			let temp=arguments[0];
			console.log(temp);
			if(temp.type==='end')
			{
				return a.push(temp.value);
			}
			if(temp.type==='in')
			{
		//	let temp=arguments[0];
			//console.log(a);
			a.push(temp.value);
			//console.log(a);
			g(temp.left);
			//console.log(a);
			g(temp.right);
			//console.log(a);
			
			}
			return a;


		}
	}
	if(type==='post')
	{
		console.log(type);
		return g = function(){

			let temp=arguments[0];
			console.log(temp);
			if(temp.type==='end')
			{
				return a.push(temp.value);
			}
			else
			{
		//	let temp=arguments[0];
			//console.log(a);
			//a.push(temp.value);
			//console.log(a);
			g(temp.left);
			//console.log(a);
			g(temp.right);
			//console.log(a);
			a.push(temp.value);
			
			}
			return a;


		}
	}
	//console.log(a);
	//return a;
	if(type==='in')
	{
		console.log(type);
		return g = function(){

			let temp=arguments[0];
			console.log(temp);
			if(temp.type==='end')
			{
				return a.push(temp.value);
			}
			else
			{
		//	let temp=arguments[0];
			//console.log(a);
			//a.push(temp.value);
			//console.log(a);
			g(temp.left);
			a.push(temp.value);
			//console.log(a);
			g(temp.right);
			//console.log(a);
			
			
			}
			return a;


		}
	}

}


function hangman(phrase) {

    const gameOver = "Game over!!!";
    const won = "You\'ve got it!!! Final phrase:";
    const wrong = "Incorrect guess!!!";
    const lost = "You\'ve lost!!! Correct phrase:";

    var count=3;
    var len=phrase.length;
    var a = [];
    var b= [];
    for(var i=0;i<phrase.length;i++)
    {
    	a[i]="_";
    }
    var main=0;

    return g = function(){
    	var temp=arguments[0];
    	var flag=0;
    	var ga=0;
    	
    //	console.log(flag);
    //	console.log(main);
    //	console.log(a);
    	/*if(count===1&&len!==0)
    	{
    		return lost+phrase;
    	}
    	if(len===0)
    	{
    		return won+phrase;
    	}*/
    	for(var k=0;k<b.length;k++)
    	{
    		if(b[k]===temp)
    			ga=1;
    	}
    	if(main===1)
    	{
    		return gameOver;
    	}
    	for(var j=0;j<phrase.length;j++)
    	{

    		if(phrase[j]===temp)
    		{
    			if(ga!==1)
    			{
    			//console.log(phrase[j]);
    				a[j]=temp;
    				len--;
    				flag=1;
    			}
    			else
    			{
    				return a.join(' ');
    			}
    		}
    	}
    	
    	/*if(ga!==1)
    	{*/
    		if(flag===0)
    		{
    			count--;
    			if(count>=1)
    			{
    				//count--;
    				b.push(temp);
    				return wrong;
    			}
    			if(count===0)
    			{
    				main=1;
    				b.push(temp);
    				return lost+" "+phrase;
    			}
    		}
    		if(flag===1)
    		{
    			if(len!==0)
    			{
    				b.push(temp);
    				return a.join(' ');
    			}
    			else
    			{
    				main=1;
    				b.push(temp);
    				return won+" "+phrase;
    			}
    		}
    	//}
    	/*else
    	{
    		return wrong;
    	}*/
    	

    }
    //return g;

}

function Person(name, age) {
	//var Person = function(name,age){
		this.name=name;
		this.age=age;
	}
Person.prototype.about=function()
{
	return 'My name is'+' '+this.name+' '+'and I\'m'+' '+this.age+' '+'yrs old.'
};



function Student(name, age, roll) {
	Person.call(this, name, age);
	this.roll=roll;
}
Student.prototype.id=function()
{
	return 'Student Id:'+' '+this.roll;
}
Student.prototype.__proto__ = Person.prototype;

const numberList = {
	 
		numbers: [],
		set add(num){
			this.numbers.push(num);
		},
		get sum()
		{
			var result=0;
			for(var i=0;i<this.numbers.length;i++)
				result+=this.numbers[i];
			return result;
		},
		get average()
		{
			/*var result2=0;
			for(var i=0;i<this.numbers.length;i++)
				result2+=this.numbers[i];
			return result2/(this.numbers.length);*/
			return (this.sum)/(this.numbers.length);
		}
	

};


function carRace(cars,finish) {

//console.log(cars);
	Promise.race(cars)
	.then(function(val){ finish(val.name+' '+'won in'+' '+val.time+' '+'seconds!!!')});
  
	

}

module.exports = {
    myArrayFilter,
    myArrayReduce,
    myTreeReduce,
    myTreeSize,
    myTreeTraversal,
    hangman,
    Person,
    Student,
    numberList,
    carRace
};
