const mongoose = require('mongoose');


//dont really need the schema...
const schema = new mongoose.Schema({
	_id : mongoose.Schema.Types.ObjectId,
	title : String,
	link: String,
	date: String,
});

//sources
const sources = ['kurir','blic','alo','b92','srbijadanas','espreso',
		'informer','n1', 'telegraf', 'novosti','danas'];
		
//logos locations
const logo = {
	'kurir' : 'https://www.kurir.rs/resources/images/header/logo.svg?v2',
	'blic' : 'https://upload.wikimedia.org/wikipedia/sh/f/ff/%D0%91%D0%BB%D0%B8%D1%86_%D0%BB%D0%BE%D0%B3%D0%BE.jpg',
	'alo' : 'https://www.alo.rs/resources/css/images/alo-logo-new.png',
	'b92' : 'https://tse2.mm.bing.net/th?id=OIP.WSoJR4QjsPs00lu3F1nxtQHaFj&pid=Api',
	'srbijadanas' : 'https://www.srbijadanas.com/sites/all/themes/sd_ea/logo.png', 
	'espreso' : 'https://tse4.mm.bing.net/th?id=OIP.Wz7IoUpK9URUDgFGuB84-gHaE_&pid=Api',
	'informer' : 'http://informer.rs/template/img/logo-informer.svg?v=5', 
	'n1' : 'https://upload.wikimedia.org/wikipedia/en/1/14/N1teleLogo.jpg',
	'telegraf' : 'https://tse2.mm.bing.net/th?id=OIP.e2rMhuJ7-EJj0OufW8KW-gHaE8&pid=Api',
	'novosti' :  'https://upload.wikimedia.org/wikipedia/en/thumb/9/90/Ve%C4%8Dernje_novosti.svg/1200px-Ve%C4%8Dernje_novosti.svg.png',
	'danas' : 'http://www.cenzolovka.rs/wp-content/uploads/2015/06/Danas-logo.jpg',
};

//date_string 2020-09-04

const today = new Date();
const day = today.getDate(), year = today.getFullYear(), month = today.getMonth();

const def = year + '-' + (month + 1 < 10 ? '0' + (month + 1) : month + 1) + '-' + (day < 10 ? '0' + day : day);

// console.log(def);

module.exports.getData = async function (date_string = def) {
	
	let res = [];
	try {
		for(let i = 0; i < sources.length; i++) {
			let News = mongoose.model(sources[i], schema, sources[i]);
			
			const query = {
				date: date_string
			}
			//console.log(query);
			const curr = await News.find(query).exec();
			//copying - concat not working here
			res.push(curr);
		}
		
		return {
			news : res,
			origin : sources,
			logos : logo
		};
		
	}catch(err){
		console.log(err);
	}
	
}
