document.addEventListener('DOMContentLoaded', function() {
  // Seleccionar todos los enlaces con la clase 'close' dentro de los mensajes
  var closeButtons = document.querySelectorAll('.block-message .close');

  // Añadir un event listener a cada botón de cierre
  closeButtons.forEach(function(button) {
    button.addEventListener('click', function(e) {
      e.preventDefault(); // Prevenir el comportamiento predeterminado del enlace
      var blockMessage = this.closest('.block-message'); // Encontrar el mensaje más cercano
      if (blockMessage) {
        blockMessage.style.display = 'none'; // Ocultar el mensaje
      }
    });
  });
});
