<div align="center">
 <h1>Perhitugan-GJB-menggunakan-YOLOV3</h1>
 <img src="https://user-images.githubusercontent.com/75331373/219564185-6d73f9d2-72bf-421c-a78c-328d7b7ac146.png" alt="Open In Colab">
 <p>Sumber gambar = Jurnal YOLOV3 Joseph Redmon
</div>

<div align="center">
 <h1>Dataset</h1>
Berisi <strong> Classes.names </strong> yang berisikan daftar kelas dalam format yang fleksibel. Kelas yang terdapat pada repository ini adalah
</div>
<br>
<ol>
 <li>Dog (Anjing)</li>
 <li>Person (Orang) </li>
 <li>Cat (Kucing)</li>
 <li>TV</li>
 <li>Car (Mobil)</li>
 <li>Meatballs (Bakso)</li>
 <li>Marina Sauce (Saus Marina)</li>
 <li>Tomato soup (Sup tomat)</li>
 <li>Chicken noodle soup</li>
 <li>French Onion Soup</li>
 <li>Chicken breast</li>
 <li>Ribs</li>
 <li>Pulled pork</li>
 <li>Hamburger</li>
 <li>Cavity</li>
 <li>Bola GJB</li>
 <li>Pemabatas</li>
</ol>
<br>
<strong>Dataset Custom</strong> terdiri dari
<ol>
 <li><strong>500++</strong> Dataset Bola GJB dan pembatas dengan format <strong>jpg</strong?</li>
 <li>File dengan format txt </li>
</ol>

<div align="center">
 <h1> Langkah langkah </h1>
</div>

1. Label data menggunakan cara yang ada pada folder <strong> labelimg </strong>
2. Training dengan menggunakan file <strong>0. Training dataer.ipynb</strong> menggunakan google colab
3. Mendownload cfg dan weights
4. Deteksi dengan menggunakan file <strong> 7. YOLOV3(Berhasil) </strong>
