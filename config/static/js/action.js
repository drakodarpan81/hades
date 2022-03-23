const btnsAgregar = document.querySelectorAll("#btnTest");
const btnsDelete = document.querySelectorAll("#btnDelete");

(function(){
    btnsAgregar.forEach((btn) => {
        btn.addEventListener("click", function(e){
            e.preventDefault();
            console.log(e.target.href);
            Swal.fire({
                title: '¿Desea grabar el registro?',
                showCancelButton:true,
                confirmButtonText:"Guardar",
                confirmButtonColor:"#B0E6B2",
                backdrop:true,
                showLoaderOnConfirm:true,
                preConfirm:()=>{
                    location.href = e.target.href;
                },
                allowOutsideClick: ()=>false,
                allowEscapeKey:()=>false,
            });
        });
    });

    /*
    btnsDelete.forEach((btn) => {
        btn.addEventListener("click", function(e){
            e.preventDefault();
            console.log(window.location.pathname);
            Swal.fire({
                title: '¿Desea eliminar el registro?',
                showCancelButton:true,
                confirmButtonText:"Guardar",
                confirmButtonColor:"#B0E6B2",
                backdrop:true,
                showLoaderOnConfirm:true,
                preConfirm:()=>{
                    //location.href = window.location.pathname;
                },
                allowOutsideClick: ()=>false,
                allowEscapeKey:()=>false,
            });
        });
    });
    */
   
})();
