//Creates a list for the items currently in the to do list
let toDo = []

//Adds an item to the to do list after clicking btn1
document.getElementById("btn1").addEventListener("click", addItemToList)

function addItemToList () {
    //Creates elements for the newly added item 
    let item = document.getElementById("item");
    let list = document.createElement("p");
    let btn = document.createElement("BUTTON");
    let div = document.createElement("div");
    //Checks to see that the item added isn't a blank space
    if (!(/^\s*$/.test(item.value))) {
        //Makes sure added item doesn't already exist within the list
        if (toDo.indexOf(item.value) == -1) {
            createP(item.value, list);
            createB(item.value, btn);
            div.appendChild(list);
            div.appendChild(btn);
            document.getElementById("list").appendChild(div);
        }
    //Resets the text box for the user to enter another item
    document.getElementById("form").reset()
    }
}

//Takes in a <p> and added the proper classes and text
function createP (i, element) {
    toDo.push(i);
    element.innerText = i;
    element.classList.add("all_p");
}

//Takes in a <button> and adds the proper texts and utility to it
function createB (i, button) {
    let num = toDo.indexOf(i)
    button.setAttribute("id", num)
    button.classList.add("all_btn");
    button.appendChild(document.createTextNode("X"));
    button.addEventListener("click", removeItem);
}

//Removes the item from toDo list and the UI
function removeItem() {
    let btn = document.getElementById(this.id);
    toDo[this.id] = null;
    btn.parentElement.remove();
}

//Adds utility to btn2
document.getElementById("btn2").addEventListener("click", removeAllItems)

//Removes all items in the toDo list and the UI list
function removeAllItems() {
    let list = document.getElementById("list")
    let child_one = list.getElementsByTagName("div")
    while(child_one.length > 0) {
        list.removeChild(child_one[0])
    }
    toDo = []
}
