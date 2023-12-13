namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        private Microsoft.DirectX.Direct3D.Device device;
        private Microsoft.DirectX.Direct3D.Texture texture;
        private Microsoft.DirectX.Direct3D.Font font;

        public Form1()
        {
            InitializeComponent();
            InitDevice();
            InitFont();
            LoadTexture();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
        private void InitFont()
        {
            System.Drawing.Font f = new System.Drawing.Font("Arial", 16f, FontStyle.Regular);
            font = new Microsoft.DirectX.Direct3D.Font(device, f);
        }
        private void LoadTexture()
        {
            texture = TextureLoader.FromFile(device, "E:\\design assignment\\glass.jpg", 400, 400, 1, 0, Format.A8B8G8R8, Pool.Managed, Filter.Point, Filter.Point, Color.Transparent.ToArgb());
        }
        private void InitDevice()
        {
            PresentParameters pp = new PresentParameters();
            pp.Windowed = true;
            pp.SwapEffect = SwapEffect.Discard;
            device = new Device(0, DeviceType.Hardware, this, CreateFlags.HardwareVertexProcessing, pp);
        }


        private void Render()
        {
            device.Clear(ClearFlags.Target, Color.Cyan, 0, 1);
            device.BeginScene();
            using (Sprite s = new Sprite(device))
            {
                s.Begin(SpriteFlags.AlphaBlend);
                s.Draw2D(texture, new Rectangle(0, 0, 0, 0), new Rectangle(0, 0, device.Viewport.Width, device.Viewport.Height), new Point(0, 0), 0f, new Point(0, 0), Color.White);
                font.DrawText(s, "Game Programming", new Point(0, 0), Color.Red);
                s.End();
            }
            device.EndScene();
            device.Present();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Render();
        }
    }
}
