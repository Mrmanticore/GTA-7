namespace WindowsFormsApplication2
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
            CustomVertex.TransformedColored[] v = new CustomVertex.TransformedColored[3];

            v[0].Position = new Vector4(240, 110, 0, 1);
            v[0].Color = System.Drawing.Color.FromArgb(255, 0, 0).ToArgb();

            v[1].Position = new Vector4(380, 420, 0, 1);
            v[1].Color = System.Drawing.Color.FromArgb(0, 255, 0).ToArgb();

            v[2].Position = new Vector4(110, 420, 0, 1);
            v[2].Color = System.Drawing.Color.FromArgb(0, 0, 255).ToArgb();

            d.Clear(ClearFlags.Target, Color.CornflowerBlue, 0, 1);
            d.BeginScene();
            d.VertexFormat = CustomVertex.TransformedColored.Format;
            d.DrawUserPrimitives(PrimitiveType.TriangleList, 1, v);
            d.EndScene();
            d.Present();
        }

       
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Render();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }

}
