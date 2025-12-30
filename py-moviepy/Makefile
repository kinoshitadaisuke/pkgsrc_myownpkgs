# $NetBSD$

DISTNAME=	moviepy-2.2.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	multimedia python
MASTER_SITES=	${MASTER_SITE_PYPI:=m/moviepy/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/moviepy/
COMMENT=	Video editing with Python
LICENSE=	mit

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-decorator>=4.0.2:../../devel/py-decorator
DEPENDS+=	${PYPKGPREFIX}-imageio>=2.5:../../graphics/py-imageio
DEPENDS+=	${PYPKGPREFIX}-imageio-ffmpeg>=0.2:../../pkgsrc_myownpkgs/py-imageio-ffmpeg
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.25:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-proglog>=0:../../pkgsrc_myownpkgs/py-proglog
DEPENDS+=	${PYPKGPREFIX}-dotenv>=0.10:../../devel/py-dotenv
DEPENDS+=	${PYPKGPREFIX}-Pillow>=9.2.0:../../graphics/py-Pillow
DEPENDS+=	opencv>=4.0.0:../../graphics/opencv

.include "../../graphics/opencv/buildlink3.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
