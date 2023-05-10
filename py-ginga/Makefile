# $NetBSD$

DISTNAME=	ginga-4.0.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=g/ginga/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://ginga.readthedocs.io/
COMMENT=	Astronomical image viewer and toolkit
LICENSE=	modified-bsd

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=6.2:../../devel/py-setuptools_scm
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.14:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-astropy>=5.0:../../math/py-astropy
DEPENDS+=	${PYPKGPREFIX}-scipy>=0.18.1:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-Pillow>=6.2.1:../../graphics/py-Pillow
#DEPENDS+=	${PYPKGPREFIX}-opencv-python>=4.7:../../pkgsrc_myownpkgs/py-opencv-python
#DEPENDS+=	opencv-[0-9]*:../../graphics/opencv
DEPENDS+=	${PYPKGPREFIX}-piexif-[0-9]*:../../graphics/py-piexif
DEPENDS+=	${PYPKGPREFIX}-beautifulsoup4>=4.3.2:../../www/py-beautifulsoup4
DEPENDS+=	${PYPKGPREFIX}-docutils-[0-9]*:../../textproc/py-docutils
DEPENDS+=	${PYPKGPREFIX}-gwcs-[0-9]*:../../pkgsrc_myownpkgs/py-gwcs
DEPENDS+=	${PYPKGPREFIX}-QtPy>=2.0.1:../../pkgsrc_myownpkgs/py-qtpy
#DEPENDS+=	${PYPKGPREFIX}-pyside-[0-9]*:../../wip/py-pyside
#DEPENDS+=	${PYPKGPREFIX}-gobject-[0-9]*:../../devel/py-gobject
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=2.1:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-tornado-[0-9]*:../../www/py-tornado
DEPENDS+=	${PYPKGPREFIX}-exifread>=2.3.2:../../graphics/py-exifread
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>0:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-magic>=0.4.15:../../sysutils/py-magic
DEPENDS+=	${PYPKGPREFIX}-astroquery>=0.3.5:../../pkgsrc_myownpkgs/py-astroquery
DEPENDS+=	${PYPKGPREFIX}-photutils>0:../../pkgsrc_myownpkgs/py-photutils
DEPENDS+=	${PYPKGPREFIX}-attrs>=19.2.0:../../devel/py-attrs
DEPENDS+=	${PYPKGPREFIX}-cairo>0:../../graphics/py-cairo
DEPENDS+=	${PYPKGPREFIX}-qt5>0:../../x11/py-qt5

CHECK_INTERPRETER=	no

post-extract:
	${CHMOD} -R go-w ${WRKSRC}

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
