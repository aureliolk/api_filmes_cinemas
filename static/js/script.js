let url_api = 'https://api-cinema-acos.herokuapp.com/api/filmes'
$(function(){
	$.ajax({
		url:url_api,
		type:'GET',
		dataType:'json',
		beforeSend:function(){
			$('.filmes').html("<div class='col-md-12'>Carregano</div>")
		},
		success:function(json){
			let html = ''
			for (let i in json.filmes){
				html += '<div class="col-md-4 p-2"><h4 class="mb-2">'+json.filmes[i].title+'</h4><img class="img img-fluid" src='+json.filmes[i].img_src+'></div>'
				// console.log(json.filmes[i].title, json.filmes[i].img_src)
			}
			$('.filmes').html(html)
		}
	})
})