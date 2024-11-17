import axios from 'axios';

const downloadFile = async (name: string) => {
    try {
        // Отправляем запрос на API
        const response = await axios.get('/api/files/' +name+ '.csv', {
            responseType: 'blob', 
            headers: {
              Authorization: 'Bearer ' + localStorage.getItem('token')
            }
        });

        // Создаем URL из бинарных данных
        const blob = new Blob([response.data], { type: 'text/csv' });
        const url = window.URL.createObjectURL(blob);

        // Создаем ссылку для скачивания
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download',name +  '.csv'); // Название файла
        document.body.appendChild(link);

        // Кликаем по ссылке для скачивания
        link.click();

        // Убираем ссылку из DOM
        link.remove();

        // Освобождаем память
        window.URL.revokeObjectURL(url);
    } catch (error) {
        console.error('Ошибка при скачивании файла:', error);
    }
};

export default downloadFile;
