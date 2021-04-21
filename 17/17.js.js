const cheerio = require("cheerio");
const axios = require("axios");

async function fetchHtmlTagText(url, tag) {
  const response = await axios.get(url);
  return cheerio.load(response.data)(tag).text();
}

async function getSumWrittenNumbersLength(start, end, writtenNumbers = []) {
  if (start > end) return writtenNumbers.map((writtenNumber) => writtenNumber.replace(/[- ]/g, "").length).reduce((x, y) => x + y);
  return getSumWrittenNumbersLength(start + 1, end, [...writtenNumbers, await fetchHtmlTagText(`https://www.numwrite.com/${start}-number-english.html`, "p")]);
}

(async () => console.log(await getSumWrittenNumbersLength(1, 5)))(); //It probably would work but don't try it tho
