var APIURL = "http://localhost:8000/"
var items = []
var query = "";
var date = new Date();
var changed = false;

var setItems = function(query){
    d3.json(APIURL+query,function(error,data){
        // logging
        if(error){
            return console.warn(error);
        }

        // unixtimeを変換してitemsにpush
        for(var i=items.length;i<data.messages.length;i++){
            var dataTime = new Date(data.messages[i].time * 1000);
            data.messages[i].time = dataTime.toLocaleDateString() + " " + dataTime.toLocaleTimeString("ja-JP");
            items.push(data.messages[i]);
        }
    });
    return items;
};

// message list component
var MessageList = {
    data:function(){
        setItems(query);
        return {items:items};
    },
    template:"#message-list"
}

// input form component
var MessageForm = {
    data:function(){
        return {name:"",msg:""}
    },
    template:"#message-form",
    methods:{
        pushDataBase:function(){
            var post_time = date.getTime();
            post_time = Math.floor( post_time / 1000 );
            POST_URL = APIURL+"post/"+this.name+"&"+post_time+"&"+this.msg;
            fetch(POST_URL);
            setItems("");
            this.msg = "";
        }
    }
}

new Vue({
    el:"#app",
    created:function(){
        setInterval(() => setItems(""), 10000);
    },
    components:{
        MessageList:MessageList,
        MessageForm:MessageForm
    }
});