from fpdf import FPDF

# Create a PDF object
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add content
content = """
Question Three: File Systems

A. Discuss Special Purpose, Distributed File Systems, and Disk-Based File Systems:

1. Special Purpose File Systems:
   - These are designed for specific applications or environments. For example:
     - procfs (Process File System): Used in Unix-like systems to provide information about running processes.
     - tmpfs (Temporary File System): Stores files in memory for fast access, typically used for temporary files.

2. Distributed File Systems:
   - These allow files to be shared across multiple nodes in a network. Examples include:
     - NFS (Network File System): Allows remote file access over a network as if they were local.
     - HDFS (Hadoop Distributed File System): Designed for big data applications, it stores large files across multiple machines.

3. Disk-Based File Systems:
   - These manage files stored on physical disks. Examples include:
     - FAT (File Allocation Table): A simple file system used in older Windows systems and removable media.
     - NTFS (New Technology File System): A modern file system used in Windows with advanced features like journaling and security.
     - ext4 (Fourth Extended File System): Commonly used in Linux systems, offering high performance and reliability.

B. Benefits and Limitations of NTFS over FAT:

Benefits of NTFS:
1. Security: NTFS supports file permissions and encryption, providing better security for sensitive data.
2. Reliability: NTFS includes journaling, which helps recover data after a system crash or power failure.
3. Large File and Volume Support: NTFS supports very large files (up to 16 TB) and volumes (up to 256 TB), making it suitable for modern storage needs.
4. Efficiency: NTFS uses advanced data structures like B-trees for file indexing, improving performance for large directories.
5. Compression and Quotas: NTFS supports file compression and disk quotas, allowing better storage management.

Limitations of NTFS:
1. Compatibility: NTFS is less compatible with non-Windows operating systems, making it harder to access files on systems like macOS or Linux without additional software.
2. Overhead: NTFS has more overhead compared to FAT, which can be a disadvantage on very small storage devices like USB drives.
3. Complexity: The advanced features of NTFS make it more complex to implement and manage compared to FAT.

Question Four: Input/Output Management

B. Five Objectives of Input/Output (I/O) Management Function:

1. Efficiency: Maximize the efficiency of I/O operations to ensure that the CPU and devices are utilized optimally.
2. Device Independence: Provide a uniform interface for accessing different types of devices, allowing applications to interact with devices without needing to know their specific details.
3. Error Handling: Detect and recover from I/O errors, ensuring data integrity and system stability.
4. Synchronization: Ensure proper synchronization between I/O operations and processes to avoid conflicts and data corruption.
5. Buffering: Use buffers to smooth out speed differences between devices and the CPU, improving overall system performance.

C. Categories of I/O Devices:

(i) Character-Oriented Devices:
- Example: Keyboard, mouse.
- Explanation: These devices handle data one character at a time. For example, a keyboard sends individual keystrokes to the system.

(ii) Block-Oriented Devices:
- Example: Hard drives, SSDs.
- Explanation: These devices handle data in fixed-size blocks. For example, a hard drive reads and writes data in sectors, typically 512 bytes or 4 KB in size.

(iii) Communication Devices:
- Example: Network cards, modems.
- Explanation: These devices handle data transmission between computers or networks. For example, a network card sends and receives data packets over a network.
"""

# Add the content to the PDF
pdf.multi_cell(0, 10, content)

# Save the PDF to a file
pdf.output("question3_question4_answers.pdf")

print("PDF created successfully: question3_question4_answers.pdf")