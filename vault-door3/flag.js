password = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
// password = "jU5t_a_sna_3lpm1dg347_u_4_mfr54b"
var i;
var buffer = Array(32);

for (i = 0; i < 8; i++) {
      buffer[i] = password.charAt(i)
}

for (; i < 16; i++) {
      buffer[i] = password.charAt(23 - i)
}
for (; i < 32; i += 2) {
      buffer[i] = password.charAt(46 - i)
}
for (i = 31; i >= 17; i -= 2) {
      buffer[i] = password.charAt(i)
}

console.log("picoCTF{" + buffer.join("") + "}");