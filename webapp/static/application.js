Dropzone.autoDiscover = false;
var dropzone = new Dropzone('#dropzone', {
  parallelUploads: 2,
  thumbnailHeight: 120,
  thumbnailWidth: 120,
  maxFilesize: 3,
  filesizeBase: 1000,
  resizeWidth: 1280
});

const error = document.querySelector('.error');
dropzone.on('error', function(_, response) {
  answer.classList.remove('hidden');
  error.textContent = 'エラーが発生しました';
});

const result = document.querySelector('.result');
const answer = document.querySelector('.answer');

dropzone.on('success', function(_, response) {
  console.log('success!', response);
  result.classList.remove('hidden');
  answer.textContent = response.name;
});
