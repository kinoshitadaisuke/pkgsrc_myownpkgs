# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-basictools-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs shells graphics math science python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for basic tools
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# security
DEPENDS+=	mozilla-rootcerts-openssl>=0:../../security/mozilla-rootcerts-openssl
DEPENDS+=	openssh>=0:../../security/openssh
DEPENDS+=	openssl>=0:../../security/openssl

# shells
DEPENDS+=	tcsh>=0:../../shells/tcsh
DEPENDS+=	zsh>=0:../../shells/zsh

# archivers
DEPENDS+=	bzip2>=0:../../archivers/bzip2
DEPENDS+=	bzip3>=0:../../archivers/bzip3
DEPENDS+=	gtar>=0:../../archivers/gtar
DEPENDS+=	unzip>=0:../../archivers/unzip
DEPENDS+=	xz>=0:../../archivers/xz
DEPENDS+=	zip>=0:../../archivers/zip

# devel
DEPENDS+=	php-mode>=0:../../devel/php-mode

# editors
DEPENDS+=	emacs29>=0:../../editors/emacs29

# fonts
DEPENDS+=	arphic-ttf>=0:../../fonts/arphic-ttf
DEPENDS+=	cyberbit-ttf>=0:../../fonts/cyberbit-ttf
DEPENDS+=	intlfonts>=0:../../fonts/intlfonts
DEPENDS+=	ipaexfont>=0:../../fonts/ipaexfont
DEPENDS+=	ipafont>=0:../../fonts/ipafont
DEPENDS+=	jisx0208fonts>=0:../../fonts/jisx0208fonts
DEPENDS+=	jisx0212fonts>=0:../../fonts/jisx0212fonts
DEPENDS+=	jisx0213fonts>=0:../../fonts/jisx0213fonts
#DEPENDS+=	noto-cjk-fonts>=0:../../fonts/noto-cjk-fonts
#DEPENDS+=	noto-fonts>=0:../../fonts/noto-fonts
DEPENDS+=	noto-ttf>=0:../../fonts/noto-ttf
DEPENDS+=	ricty-ttf>=0:../../fonts/ricty-ttf

# graphics
DEPENDS+=	ImageMagick>=0:../../graphics/ImageMagick
DEPENDS+=	feh>=0:../../graphics/feh
DEPENDS+=	gimp>=0:../../graphics/gimp
DEPENDS+=	gnuplot>=0:../../graphics/gnuplot
DEPENDS+=	netpbm>=0:../../graphics/netpbm
DEPENDS+=	tgif>=0:../../graphics/tgif
DEPENDS+=	xv>=0:../../graphics/xv

# input method
DEPENDS+=	mozc-elisp>=0:../../inputmethod/mozc-elisp
DEPENDS+=	mozc-server>=0:../../inputmethod/mozc-server
DEPENDS+=	mozc-tool>=0:../../inputmethod/mozc-tool

# lang
DEPENDS+=	perl>=0:../../lang/perl5
DEPENDS+=	python312>=0:../../lang/python312

# multimedia
DEPENDS+=	ffmpeg6>=0:../../multimedia/ffmpeg6
DEPENDS+=	mpv>=0:../../multimedia/mpv

# net
DEPENDS+=	wget>=0:../../net/wget
DEPENDS+=	wget2>=0:../../net/wget2
DEPENDS+=	yt-dlp>=0:../../net/yt-dlp

# print
DEPENDS+=	gv>=0:../../print/gv
DEPENDS+=	okular>=0:../../print/okular
DEPENDS+=	qpdf>=0:../../print/qpdf
DEPENDS+=	xpdf>=0:../../print/xpdf4

# textproc
DEPENDS+=	aspell>=0:../../textproc/aspell
DEPENDS+=	aspell-en>=0:../../textproc/aspell-en

# wm
DEPENDS+=	fvwm3>=0:../../wm/fvwm3

# www
DEPENDS+=	curl>=0:../../www/curl

# pkgsrc_myownpkgs
DEPENDS+=	yatex>=0:../../pkgsrc_myownpkgs/yatex-mode

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
