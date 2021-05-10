import React from 'react';

import { gql, useMutation } from '@apollo/client';

const UPLOAD_FILE = gql`
	mutation($file: Upload!) {
		fileUpload(file: $file) {
			success
		}
	}
`;

function App() {
	const [uploadFile, { loading, data }] = useMutation(UPLOAD_FILE);
	const { fileUpload } = data || {};
	const { success = false } = fileUpload || {};

	const handleUploadFile = React.useCallback(
		(event) => {
			event.preventDefault();
			const [file] = event.target.fileUpload.files || [];
			if (file) uploadFile({ variables: { file } });
		},
		[uploadFile]
	);

	return (
		<div>
			<h1>File upload example</h1>

			<p>Upload a file below</p>

			{loading && 'Uploading file...'}
			{success && 'File successfully uploaded!'}

			<form onSubmit={handleUploadFile}>
				<input name="fileUpload" type="file" />
				<button type="submit">Submit</button>
			</form>
		</div>
	);
}

export default App;
