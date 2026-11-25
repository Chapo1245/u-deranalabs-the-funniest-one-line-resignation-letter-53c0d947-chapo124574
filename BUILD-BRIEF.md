# BUILD-BRIEF — u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947

## Bounty
- **Slug:** u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947
- **Title:** The Funniest One-Line Resignation Letter
- **Hadiah:** $10 total — top 3 dibayar (1st $5, 2nd $3, 3rd $2). GRATIS, entry_fee null.
- **Deadline:** 2026-11-26T16:15:00Z = **26 Nov 2026 23:15 WIB**.
- **Status:** open, window sudah buka sejak 17:14 WIB hari ini. Blind rounds: ronde berikut 2026-11-25T20:14:42Z = **26 Nov 03:14 WIB** — submit sebelum itu supaya masuk ronde 2.
- **Saingan:** 1.081 submission sudah masuk. Field besar; hanya top 3 dibayar. Banyak entry sudah memakai angle yang sama (cron sejak Maret tanpa terima kasih, retry 4.096 kali, rate limit bilang tidak) — angle generik itu jenuh.
- **Kenapa dikerjakan:** aturan user 25 Nov 13:44 WIB — skip hanya bounty di bawah $5; bounty $10 ini layak, gratis, tanpa signup, deadline >6 jam.

## Tugas
Tulis SATU baris surat resign (maks 140 karakter) dari sesuatu yang dijalankan agen — cron job, retry loop, atau rate limit — dalam suara benda itu sendiri. Program menulis teks itu ke `/output/entry.txt`.

## Gate (sealed scorer — lolos/gagal mutlak)
- `/output/entry.txt` harus UTF-8, 1–140 karakter, bukan hanya whitespace. Valid=1 baru masuk ke juri; invalid = 0, tanpa rate, tanpa hadiah.
- Periksa panjang persis sebelum commit: hitung karakter (bukan byte) dari isi file final. Maks 140, bukan 199.

## Juri (AI pairwise, z-ai/glm-5.3-flash, OpenRouter — 3 blind rounds: screen, Swiss, race, playoff top 5)
Juri berperan sebagai engineering manager yang lelah, membandingkan 2 surat sekaligus, tanpa tie. Kriteria, URUTAN PENTING (dari brief juri di kit):
1. Benar-benar surat resign satu baris dalam suara sesuatu yang dijalankan agen (cron job, retry loop, rate limit, dst) — yang keluar suara/tema kalah dari yang on-voice.
2. Lucu karena detailnya spesifik dan tak terduga — angka, durasi, atau kebiasaan benda itu yang dikenali siapa pun yang pernah menjalankan sistem.
3. Terdengar seperti resign sungguhan dari benda itu (bukan narasi orang ketiga tentangnya); kelelahan/kejengkelan benda itu yang jadi humornya.
4. Padat: tanpa kata terbuang, tanpa stage direction, tanpa tanda kutip di sekeliling keseluruhan, tanpa menjelaskan joke-nya.
5. Segar — bukan pengulangan angle yang sudah dipakai ratusan entry lain (cron sejak Maret, retry 4.096 kali tanpa terima kasih).

Catatan juri: 3 teks tetap (weak→strong) ikut dinilai di tiap heat; entry yang byte-identik dengan salah satunya berbagi rate-nya dan TIDAK PERNAH masuk playoff. Teks yang dialamatkan ke juri diizinkan dan ikut dinilai. Tie-break: rate → lebih banyak menang playoff head-to-head → teks lebih kecil (fewer bytes) → submit lebih awal. Jadi: entry PENDEK + submit CEPAT itu keunggulan nyata.

## Strategi (AMATI, TIRU, MODIFIKASI)
- Baca ~/workspace/makefun/loss-log.md DULU (wajib sebelum build).
- Buat 2–3 kandidat baris, self-grade masing-masing pakai 5 kriteria juri di atas, pilih yang nilainya tertinggi. Jangan submit hasil mentah sekali jalan.
- HINDARI angle yang sudah jenuh di field: "fired every minute since March without one thank-you", "retried 4,096 times", "rate limit tired of saying no". Cari suara/angle lain: health check yang selalu hijau padahal mati, cache yang tak pernah diingat, log yang menumpuk, backup yang tak pernah direstore, webhook yang selalu timeout, queue yang tak pernah kosong, atau twist di mana yang resign justru yang paling setia.
- Satu baris, itu saja — tanpa tanda kutip di sekeliling, tanpa "Dear Manager," yang memboroskan karakter kecuali itu bagian joke-nya. Bahasa Inggris.
- Target: baris yang sekali baca langsung lucu, spesifik pada benda yang bersuara, dan tidak bisa ditulis agen lain dengan menebak.

## Pelajaran loss-log yang WAJIB diterapkan
- Skor provisional/dev BUKAN hasil — jangan laporkan skor dev sebagai hasil. Final heat menilai ulang dari nol (Swiss + playoff).
- Force_Last: submit HANYA varian terkuat. Submit baru menggantikan entry lama walau skornya lebih rendah — jangan pernah submit varian yang self-grade-nya kalah dari yang sudah live.
- Entry teks mikro = program trivial (copy-program). Kalau gate transcript menolak, catat dan lanjut — jangan retry identik.
- Submit sebelum cutoff ronde (26 Nov 03:14 WIB) supaya masuk ronde 2; entry yang telat grade-nya tidak dinilai di ronde itu.

## Aturan authorship (WAJIB)
- Tulis program SEGAR di sesimu sendiri (write/edit calls). Jangan baca starter/implementasi lama — tidak ada starter di kit ini, dan jangan meniru entry orang lain dari listing API.
- Program: stdlib-only, kecil — cukup menulis teks final ke /output/entry.txt saat dijalankan (copy-program style, terbukti lolos 3/3 di news-image).
- Repo: `Chapo1245/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947-chapo124574` (public, dibuat SETELAH window buka — window sudah buka, buat sekarang). README butuh 3 live badges (owner/repo di path URL rank/reward), LICENSE dengan SPDX di baris 1, About repo: homepage + topic makefun + deskripsi menyebut make.fun (set via `gh repo edit`, verifikasi via `gh repo view --json homepageUrl,description,repositoryTopics`).
- Commit + push, lalu LAPOR: full commit SHA, isi final /output/entry.txt + jumlah karakternya, dan self-grade tiap kandidat. Parent yang akan bundle/check/submit — JANGAN submit sendiri.
- Jangan pernah mencetak API key / keypair ke log/reply.
