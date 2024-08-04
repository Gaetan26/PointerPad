const ws = new WebSocket(`ws://${location.host}/remote`);
document.querySelectorAll(".clickable").forEach((clickable) => {
  clickable.onclick = () => {
    ws.send(clickable.dataset.keycode);
  };
});