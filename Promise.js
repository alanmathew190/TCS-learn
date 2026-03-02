async function hello() {
await new Promise((res, rej) => {
    let yes = false;
    if (yes) {
      res("Hello To you");
    } else {
      rej("No hello For you");
    }
  });
}
// hello.then((mes) => {
//     console.log(mes)
// }).catch((err) => {
//     console.log(err)
// })
// })

hello().then((res) => {
    console.log(res);
  }).catch((err) => {
    console.log(err);
  }
)