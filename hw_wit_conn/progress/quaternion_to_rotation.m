
% Step 1: Read quaternion data from a CSV file
% Assuming the CSV has columns: [w, x, y, z] for each quaternion
filename = 'quaternion_data.csv';  % Change this to your actual file name
quat_data = readmatrix(filename);   % Reads CSV into a matrix

% Initialize storage for rotation matrices
num_quats = size(quat_data, 1);
rot_matrix_data = zeros(3, 3, num_quats);  % Preallocate for efficiency

% Step 2: Loop through each quaternion, convert to rotation matrix
for i = 1:num_quats
    quat = quat_data(i, :);  % Extract each quaternion (row-wise)
    
    % Convert the quaternion to a rotation matrix
    R = quat2rotm(quat);
    
    % Store the resulting rotation matrix
    rot_matrix_data(:, :, i) = R;
    
    % Optional: Display the rotation matrix
    disp(['Rotation Matrix for Quaternion ', num2str(i), ':']);
    disp(R);
end

% Step 3: Save the rotation matrices to a MAT file
save('rotation_matrices.mat', 'rot_matrix_data');

% (Optional) Save rotation matrices to CSV format (flatten the 3D array into 2D)
flattened_rot_matrix = reshape(rot_matrix_data, [], 9);  % Each matrix is 1 row of 9 values
writematrix(flattened_rot_matrix, 'rotation_matrices.csv');  % Save to a CSV file

