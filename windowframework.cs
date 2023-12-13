namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Microsoft.DirectX.Direct3D.Device d;
        public Form1()
        {
            InitializeComponent();
            InitDevice();
        }
        private void InitDevice()
        {
            PresentParameters pp = new PresentParameters();
            pp.Windowed = true;
            pp.SwapEffect = SwapEffect.Discard;
            d = new Device(0, DeviceType.Hardware, this, CreateFlags.HardwareVertexProcessing, pp);
        }
        private void Render()
        {
            d.Clear(ClearFlags.Target, Color.Aqua, 0, 1);
            d.Present();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Render();
        }
    }
}
