
% Identify the dishes

include "globals.mzn"; 
include "project_d.dzn"; 
%nasi
int: nasi_uduk;
int: nasi_kuning;
int: nasi_putih;
%lauk utama
int: ayam_goreng;
int: ayam_panggang;
int: ayam_goreng_kecap;
int: udang_goreng;
int: mie_goreng;
int: telur_dadar;
int: telur_ceplok;
int: tempe_bacem;
int: tempe_goreng;
int: tempe_orek;
int: tahu_bacem;
int: telur_asin;
int: ati_ayam_goreng;
int: ikan_lele_goreng;
int: ikan_teri;
int: ikan_bandeng_goreng;
%sayuran
int: tumis_buncis;
int: sop_bayam;
int: kangkung;
int: bayam_bening;
int: tumis_kacang_panjang;
int: cah_toge;
int: sayur_lodeh;
int: cah_labu_siam;
int: sayur_asam;
int: acar;
%buah
int: Semangka;
int: Nanas;
int: Mangga;
int: Anggur;
int: Pisang;
int: Jeruk;
int: Apel;
int: Strawberry;
int: Alpukat;
int: Buah_Naga;
int: Salak;
int: Manggis;
int: Rambutan;
% declare the calories and cost (rupiah)
array[1..42, 1..2] of int: cal;

% decision variables
set of int: v0 = 0..42; % note the 0
set of int: v1 = 1..42; 
var v0: m_pokok;
var v0: l_utama;
var v0: sayuran;
var v0: buah;

% user input maximum sum of calories and cost
int: max_calories;
int: max_cost;

% sum of calories of the selected dishes must no exceed max_calories
var 0..sum(i in 1..42) (cal[i,1]): sum_calories;
var 0..sum(i in 1..42) (cal[i,2]): sum_cost;

solve :: int_search([m_pokok, l_utama, sayuran, buah, sum_calories], 
        first_fail, indomain_min, complete) satisfy;

constraint 
    m_pokok in {nasi_uduk, nasi_putih}
    /\
    l_utama in {ayam_goreng, ikan_bandeng_goreng}
    /\
    sayuran in {tumis_buncis, acar}
    /\
    buah in {Semangka, Rambutan}
    /\
    sum_calories = cal[m_pokok,1] + cal[l_utama,1] + cal[sayuran,1] + cal[buah,1]
    /\
    sum_calories <= max_calories
    /\
    sum_cost = cal[m_pokok,2] + cal[l_utama,2] + cal[sayuran,2] + cal[buah,2]
    /\
    sum_cost <= max_cost
;

output[
  show(sum_cost),",",
  show(sum_calories),",",
  show(m_pokok),",",
  show(l_utama),",",
  show(sayuran),",",
  show(buah)
];

