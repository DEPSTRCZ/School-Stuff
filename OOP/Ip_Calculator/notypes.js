class NetIPv4_cjs {
    constructor(ip) {
      this._ip = ip
      if (!this.isValid) {
        throw new Error("Invalid IP Address")
      }
      // Split the IP address into octets and convert them to numbers
      this._octets = this._ip.split(".").map(octet => parseInt(octet))
    }
  
    get isValid() {
      let isValid = true
  
      const octets = this._ip.split(".").map(octet => parseInt(octet))
  
      for (let octet of octets) {
        if (octet < 0 || octet > 255) {
          isValid = false
          break
        }
      }
      return isValid
    }
  
    set ip(ip) {
      this._ip = ip
    }
  
    get asString() {
      return this._ip
    }
  
    //https://interlir.com/2024/02/19/converting-ipv4-addresses-to-decimal-a-step-by-step-guide/
    // Never used reduce in my life, pretty usefull src: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce
    get asInt() {
      return this._octets.reduce(
        (acc, octet, index) => acc + octet * Math.pow(256, 3 - index),
        0
      )
    }
  
    get asBinaryString() {
      // Cycle through each octet, convert to binary, and pad with 0s to 8 bits (Octet is 8 bits)
      return this._octets
        .map(octet => octet.toString(2).padStart(8, "0"))
        .join(".")
    }
  
    // Explanation not needed :D
    getOctet(index) {
      return this._octets[index]
    }
  
    // https://www.meridianoutpost.com/resources/articles/IP-classes.php Also "readable"
    getClass() {
      const firstOctet = this._octets[0]
      if (firstOctet >= 1 && firstOctet <= 127) {
        return "A"
      } else if (firstOctet >= 128 && firstOctet <= 191) {
        return "B"
      } else if (firstOctet >= 192 && firstOctet <= 223) {
        return "C"
      } else if (firstOctet >= 224 && firstOctet <= 239) {
        return "D"
      } else if (firstOctet >= 240 && firstOctet <= 255) {
        return "E"
      } else {
        return "Unknown/Error"
      }
    }
  
    // Check if the first octet is in the range of private IP addresses
    isPrivate() {
      return (
        this._octets[0] === 10 ||
        this._octets[0] === 127 ||
        (this._octets[0] === 192 && this._octets[1] === 168) ||
        (this._octets[0] === 172 &&
          this._octets[1] >= 16 &&
          this._octets[1] <= 31)
      )
    }
  }
  
  /*interface IAddressIPv4
  {
      public function __construct(string $address);
      public function isValid(): bool; OK
      public function set(string $address): IAddressIPv4; OK
      public function getAsString(): string;
      public function getAsInt(): int;
      public function getAsBinaryString(): string;
      public function getOctet(int $number): int;
      public function getClass(): string;
      public function isPrivate(): bool;
  
  }
  */
  
  const testIPs_cjs = [
    "192.168.0.1",
    "255.255.255.255",
    "10.0.0.1",
    "172.16.0.1",
    "127.0.0.1",
    "192.0.2.1",
    "256.256.256.256"
  ]
  
  testIPs_cjs.forEach(ip => {
    const net = new NetIPv4_cjs(ip)
    console.log(`Testing IP: ${ip}`)
    console.log(`isValid: ${net.isValid}`)
    console.log(`asString: ${net.asString}`)
    console.log(`asInt: ${net.asInt}`)
    console.log(`asBinaryString: ${net.asBinaryString}`)
    console.log(`getOctet(0): ${net.getOctet(0)}`)
    console.log(`getClass: ${net.getClass()}`)
    console.log(`isPrivate: ${net.isPrivate()}`)
    console.log("-------------------")
  })
  