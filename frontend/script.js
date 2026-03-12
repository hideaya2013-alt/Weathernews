const btn = document.getElementById('btn');
const setcity = document.getElementById('setcity');
const selectcity = document.getElementById('selectcity');

fetch(`frontend/city.json`)//ファイルを読みに行く
.then(res => res.json())//fetch した直後のデータは「生のレスポンス（通信結果）」という状態です。配列（オブジェクトに変換）
.then(citeis =>{
    citeis.forEach(city =>{
　　　　//変換されたデータ（cities）は、配列になっています
       //forEach を使い、配列の中身（名古屋市、岐阜市…）を 1つずつ順番に 取り出して、以下の処理を繰り返します。
        const option = document.createElement('option');// ① <option>タグを新しく作る
        option.value = city.id; // ② <option value="230010"> のようにIDを入れる
        option.innerText = city.name; // ③ <option>名古屋市</option> のように名前を入れる
        selectcity.appendChild(option); //④<select>タグの中に完成した<option>を合流させる
    });
});

btn.addEventListener('click',()=>{
    const num = selectcity.selectedIndex;
    //プルダウンリストの中に含まれるすべての<option>要素を格納
    const selectedOption = selectcity.options[num];
　　//表示用のテキストを取得
    const getcityName = selectedOption.innerText;
    //バックエンドに渡すための独自IDを取得
    const getcityID = selectedOption.value;
    //const getcityID = selectedOption.dataset.id; //cityidの値を取得
    //画面に表示
    setcity.innerText = `名称: ${getcityName} (ID:${getcityID})`;
    //バックエンドに送信する処理（例:fetch関数など）を呼ぶ
    console.log ("送信するID;", getcityID);
    fetch(`/api/Weather?getcityID=${getcityID}`)
     .then(res => res.json())
     //.then(data => console.log(data));
     .then(data => {
      console.log(data);
      document.getElementById('published_at').innerText = data.published_at;  
      document.getElementById('description').innerText = data.description;
      document.getElementById('icon').src = data.forecasts[0].icon_url;
     });
});


/*データの流れ（4ステップ）
JSON → 配列 (cities)
cities は、JSONの中身が全部入った「名簿（配列）」そのものです。
配列 → 個別のデータ (city)
cities.forEach(city => { ... }) の部分で、名簿から1行分だけ取り出して、それを city という変数に入れます。
1回目のループ：city は {"id": "230010", "name": "名古屋市"}
2回目のループ：city は {"id": "210010", "name": "岐阜市"} ...という具合です。
個別のデータ → 新しいタグ (option)
document.createElement('option') で空のタグを生成し、そこに city の中身を流し込みます。
option.value = city.id; （IDをコンピュータ用の値としてセット）
option.innerText = city.name; （都市名を人間が見る文字としてセット）
タグ → セレクトボックス (selectcity)
完成した <option> を、実際の画面（selectcity）にガチャンと合体させます。*/