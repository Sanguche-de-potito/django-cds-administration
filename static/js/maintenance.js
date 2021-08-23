document.querySelector("#artista").addEventListener("click", function () {
  obtainData("artista");
});

document.querySelector("#genero").addEventListener("click", function () {
  obtainData("genero");
});

document.querySelector("#sello").addEventListener("click", function () {
  obtainData("sello");
});

function obtainData(value) {
  let url = `http://localhost:8000/maintenance/serialize/${value}`;
  const xhttp = new XMLHttpRequest();
  xhttp.open("GET", url, true);
  xhttp.send();

  xhttp.onreadystatechange = function () {
    if (this.status == 200 && this.readyState == 4) {
      let data = JSON.parse(this.responseText);
      let res = document.querySelector("#res");
      res.innerHTML = "";
      let i = 0;

      for (let item of data) {
        res.innerHTML += `
          <tr>
            <td>${item.fields.nombre}</td>
          </tr>
        `;
        res.innerHTML += `
            <td>
                <a class="btn btn-primary" href="http://localhost:8000/maintenance/${value}/editar/${item.pk}">editar</a>
                <a class="btn btn-danger" href="http://localhost:8000/maintenance/${value}/eliminar/${item.pk}">eliminar</a>
            </td>`;
      }
      res.innerHTML += `
      <div class="pt-5">
      <a class="btn btn-primary" href="http://localhost:8000/maintenance/${value}/create/">Crear</a>
      </div>`;
    }
  };
}
