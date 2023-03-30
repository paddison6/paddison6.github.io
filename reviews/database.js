const firebaseConfig = {
apiKey: "AIzaSyAjaIQhUv2_G7mwZ5UMFhoK9WYLqbSkdRk",
authDomain: "soup-there-it-is.firebaseapp.com",
databaseURL: "https://soup-there-it-is-default-rtdb.firebaseio.com/",
projectId: "soup-there-it-is",
storageBucket: "soup-there-it-is.appspot.com",
messagingSenderId: "301588041296",
appId: "1:301588041296:web:6efcb8069ab8be3fc5cb55"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
// Initialize Realtime Database and get a reference to the service
const database = firebase.database();

function getCommentDateFromEpochs(epochs) {
    var d = new Date(epochs);
    const month = ["January","February","March","April","May","June","July","August","September","October","November","December"];
    return d.getDate().toString().padStart(2, '0') + " " + month[d.getMonth()] + " " + d.getFullYear() + " " + d.getHours().toString().padStart(2, '0') + ":" + d.getMinutes().toString().padStart(2, '0') + ":" + d.getSeconds().toString().padStart(2, '0')
}

function writeCommentData() {
    var username = $("#comment-username").val();
    if (username === "") {
        return;
    }
    var comment = $("#comment-user-comment").val();
    if (comment === "") {
        return;
    }
    var now = new Date().getTime();
    var postID = $("#post-id").val();
    if (postID === "") {
        return;
    }
    firebase.database().ref('comments/' + postID + "/" + now + "/").set({
      username: username,
      comment: comment
    });
    $("#comment-username").val("");
    $("#comment-user-comment").val("");
}

function htmlEncode(str){
    return String(str).replace(/[^\w. ]/gi, function(c){
        return '&#'+c.charCodeAt(0)+';';
    });
}

function getCommentsAndInsert() {
    var postID = $("#post-id").val();
    var allCommentsRef = firebase.database().ref('comments/' + postID);
    var commentSectionDiv = $("#comment-sec-id")[0];
    allCommentsRef.on('value', (snapshot) => {
        const allComments = snapshot.val();
        for (let timestamp in allComments) {
            var time = getCommentDateFromEpochs(parseInt(timestamp));
            var username = htmlEncode(allComments[timestamp].username);
            var comment = htmlEncode(allComments[timestamp].comment);
            var check = $("#" + timestamp);
            if (check.length != 0) {
                $("#" + timestamp + "-" + "blockquote")[0].innerHTML = comment;
                $("#" + timestamp + "-" + "figcaption")[0].innerHTML = username + " @ " + time;
                continue;
            }

            var div = document.createElement("div");
            div.className = "comment-sec-comment";

            var fig = document.createElement("figure");
            fig.className = "bg-white p-2 rounded";
            fig.style.borderLeft = ".25rem solid #a34e78";

            var blockquote = document.createElement("blockquote");
            blockquote.className = "blockquote text-break text-wrap";
            blockquote.innerHTML = comment;
            blockquote.setAttribute("id", timestamp + "-" + "blockquote");

            var figcaption = document.createElement("figcaption");
            figcaption.className = "blockquote-footer mb-0 font-italic";
            figcaption.innerHTML = username + " @ " + time;
            figcaption.setAttribute("id", timestamp + "-" + "figcaption");

            fig.appendChild(blockquote);
            fig.appendChild(figcaption);
            div.appendChild(fig);
            div.setAttribute("id", timestamp);

            commentSectionDiv.appendChild(div);
        }
    });
}

getCommentsAndInsert();