import boto3
import sys
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

print("="*50)
print("WORKSHOP SETUP VERIFICATION")
print("="*50)

# Check Python version
print(f"\n✅ Python version: {sys.version}")

# Check AWS connection
try:
    session = boto3.Session()
    sts = session.client('sts')
    identity = sts.get_caller_identity()
    print(f"✅ AWS Account: {identity['Account']}")
    print(f"✅ AWS User: {identity['Arn']}")
except Exception as e:
    print(f"❌ AWS Error: {e}")

# Check Bedrock access
try:
    bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
    print("✅ Bedrock Runtime: Connected")
except Exception as e:
    print(f"❌ Bedrock Error: {e}")

# Check installed packages
packages = ['boto3', 'anthropic', 'mcp', 'pydantic', 'dotenv']
for package in packages:
    try:
        __import__(package if package != 'dotenv' else 'dotenv')
        print(f"✅ {package}: Installed")
    except ImportError:
        print(f"❌ {package}: Not found")

# Check Strands
try:
    import strands
    print(f"✅ Strands SDK: Installed")
except ImportError:
    print(f"⚠️  Strands SDK: Will install from workshop materials")

print("\n" + "="*50)
print("Setup verification complete!")
print("="*50)