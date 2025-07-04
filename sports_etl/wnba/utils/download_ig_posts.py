import instaloader

def download_latest_posts(profile_name, n_posts=5):
    L = instaloader.Instaloader(dirname_pattern="downloads/{profile}")
    try:
        profile = instaloader.Profile.from_username(L.context, profile_name)
        for i, post in enumerate(profile.get_posts()):
            if i >= n_posts:
                break
            L.download_post(post, target=profile.username)
        print(f"Downloaded {min(n_posts, i+1)} posts from @{profile_name}")
    except Exception as e:
        print(f"Error downloading from @{profile_name}: {e}")
